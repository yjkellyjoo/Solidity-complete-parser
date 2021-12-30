from antlr4_generated.SolidityParser import SolidityParser
from antlr4_generated.SolidityListener import SolidityListener


class MySolidityListener(SolidityListener):
    def __init__(self):
        self.function_strings = []
        self.function_names = []
        self.contract_names = []

    def getNodeText(self, ctx, i, var):
        for child in ctx.getChildren():
            if child.getChildCount() != 0:
                self.getNodeText(child, i, var)
            else:
                var[i] += child.getText() + ' '

    def enterContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        self.contract_names.append(ctx.identifier().getText())

    def enterFunctionDefinition(self, ctx: SolidityParser.FunctionDefinitionContext):
        if ctx.block() is not None:
            ind = len(self.function_names)

            if ctx.functionDescriptor().identifier() is not None:
                self.function_names.append(ctx.functionDescriptor().identifier().getText())
            # fallback function definition's identifier can be None
            elif "function" in ctx.functionDescriptor().getText():
                self.function_names.append("")
            # rest of the cases: constructor, fallback (with keyword) or receive. get the type and save as name.
            else:
                self.function_names.append("")
                self.getNodeText(ctx.functionDescriptor(), ind, self.function_names)

            self.function_strings.append("")
            self.getNodeText(ctx, ind, self.function_strings)

    def enterModifierDefinition(self, ctx:SolidityParser.ModifierDefinitionContext):
        if ctx.block() is not None:
            ind = len(self.function_names)

            self.function_names.append(ctx.identifier().getText())

            self.function_strings.append("")
            self.getNodeText(ctx, ind, self.function_strings)
