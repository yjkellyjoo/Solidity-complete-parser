import rsc.constants as constants
from antlr4_generated.SolidityListener import SolidityListener
from antlr4_generated.SolidityParser import SolidityParser
from antlr4_generated.SolidityVisitor import SolidityVisitor


class MySolidityVisitor(SolidityVisitor):
    def __init__(self):
        # initialize all identifiers
        self.resultMap = {}

        self.fparamIds = set()
        self.elementaryTypes = set()
        self.functionCalls = set()
        self.eventCalls = set()
        self.identifiers = set()

        self.structNames = set()
        self.contractNames = set()

    def make_resultMap(self):
        # link every Sets into the identifier Map
        self.resultMap[constants.fparam] = self.fparamIds
        self.resultMap[constants.dtype] = self.elementaryTypes
        self.resultMap[constants.funccall] = self.functionCalls

        ## struct name starting with a capital letter could be misled as an event function call.
        for struct in self.structNames:
            if struct in self.eventCalls:
                self.eventCalls.remove(struct)
        ## contract name can also be.
        for contract in self.contractNames:
            if contract in self.eventCalls:
                self.eventCalls.remove(contract)
        self.resultMap[constants.eventcall] = self.eventCalls

        self.resultMap[constants.lvar] = self.identifiers

    def visitSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        self.visitChildren(ctx)
        self.make_resultMap()
        return self.resultMap

    def visitContractPart(self, ctx:SolidityParser.ContractPartContext):
        self.visitChildren(ctx)
        self.make_resultMap()
        return self.resultMap

    def visitParameter(self, ctx:SolidityParser.ParameterContext):
        if ctx.identifier() is not None:
            self.fparamIds.add(ctx.identifier().getText())

        return self.visitChildren(ctx)

    def visitElementaryTypeName(self, ctx:SolidityParser.ElementaryTypeNameContext):
        self.elementaryTypes.add(ctx.getText())

        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx:SolidityParser.FunctionCallContext):
        func_expression = ctx.expression()
        child_count = func_expression.getChildCount()
        last_child = func_expression.getChild(child_count-1)
        functionCall = last_child.getText()
        if functionCall == '':
            return self.visitChildren(ctx)
        elif functionCall[0].isupper():         ## for event call cases before v0.4.21
            self.eventCalls.add(functionCall)
        else:
            self.functionCalls.add(functionCall)

        return self.visitChildren(ctx)

    def visitFunctionCallWithOptions(self, ctx:SolidityParser.FunctionCallWithOptionsContext):
        func_expression = ctx.expression()
        child_count = func_expression.getChildCount()
        last_child = func_expression.getChild(child_count-1)
        functionCall = last_child.getText()
        if functionCall[0].isupper():           ## for event call cases before v0.4.21
            self.eventCalls.add(functionCall)
        else:
            self.functionCalls.add(functionCall)

        return self.visitChildren(ctx)

    def visitStructDefinition(self, ctx:SolidityParser.StructDefinitionContext):
        self.structNames.add(ctx.identifier().getText())

        return self.visitChildren(ctx)

    def visitContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        self.contractNames.add(ctx.identifier().getText())
        for ihe in ctx.inheritanceSpecifier():
            self.contractNames.add(ihe.getText())

        return self.visitChildren(ctx)

    def visitIdentifier(self, ctx:SolidityParser.IdentifierContext):
        if ctx.Identifier() is not None:
            self.identifiers.add(ctx.Identifier().getText())
        else:
            self.identifiers.add(ctx.getText())
        return self.visitChildren(ctx)


class VisitSolidityListener(SolidityListener):
    def __init__(self):
        self.type_conversion_strings = []

    def getNodeText(self, ctx, i, var):
        for child in ctx.getChildren():
            if child.getChildCount() != 0:
                self.getNodeText(child, i, var)
            else:
                var[i].append(child.getText())

    def enterTypeConversion(self, ctx:SolidityParser.TypeConversionContext):
        ind = len(self.type_conversion_strings)

        self.type_conversion_strings.append([])
        self.getNodeText(ctx, ind, self.type_conversion_strings)