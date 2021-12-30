import sys
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from antlr4_generated.SolidityLexer import SolidityLexer as MySolidityLexer
from antlr4_generated.SolidityParser import SolidityParser as MySolidityParser
from MySolidityListener import MySolidityListener
from MySolidityVisitor import MySolidityVisitor


def use_listener(source_code):
    """
        listener usage example for extracting functions from the whole source code.

    :param source_code:
    :return function codes list, function names list, contract names list:
    """
    lexer = MySolidityLexer(InputStream(source_code))
    parser = MySolidityParser(CommonTokenStream(lexer))
    sys.setrecursionlimit(10 ** 7)  # prevent python recursion error
    parser.removeErrorListeners()  # remove ErrorListener to discard unnecessary error messages
    tree = parser.sourceUnit()

    walker = ParseTreeWalker()
    listener = MySolidityListener()

    walker.walk(listener, tree)  # listener has the function_strings after it's walked
    functions = listener.function_strings
    func_names = listener.function_names
    contract_names = listener.contract_names

    return functions, func_names, contract_names


def use_visitor(function_code):
    """
        visitor usage example for tokenizing and labeling function code.
        It returns a dictionary of labels.
        Currently, five labels have been implemented: FPARAM, DTYPE, FUNCCALL, EVENTCALL, VAR.

    :param function_code:
    :return list of tokens in ANTLR4 Token object form, dictionary of labels with its matching tokens:
    """
    lexer = MySolidityLexer(InputStream(function_code))
    tokens = lexer.getAllTokens()

    lexer.reset()
    visitor = MySolidityVisitor()
    parser = MySolidityParser(CommonTokenStream(lexer))
    result_map = visitor.visit(parser.contractPart())

    return tokens, result_map


if __name__ == '__main__':
    ## open example Solidity source code
    with open("./rsc/ex_contract.sol", "r", encoding='UTF-8') as f:
        source_code = f.read()

    functions, func_names, contract_names = use_listener(source_code)
    '''
        have fun with the extracted function codes list, function names list, contract names list. 
    '''

    for function in functions:
        tokens, result_map = use_visitor(function)
        '''
            have fun with the extracted tokens and dictionary of labeled tokens
        '''
        ## example of tokens usage
        for token in tokens:
            token_string = token.text   ## string form of each token
