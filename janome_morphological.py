# coding:utf-8

from janome.tokenizer import Tokenizer


def morphological_analyze(japanese):

    """

     Perform morphological analysis of Japanese
    日本語の形態素解析を行う

    :param japanese: analysis japanese object
    :return: result of analyse (List Object)
    """

    t = Tokenizer()

    parse = t.tokenize(japanese)

    return parse


if __name__ == '__main__':

    result = morphological_analyze("日本語の形態素解析を行う")

    for a in result:
        print(a)
