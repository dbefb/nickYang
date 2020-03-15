import os
import re
import collections
from nltk.tokenize import TreebankWordTokenizer

all_file = []
word_list = []
get_list = []
outcome = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
file_path = '**********'
dictionary = '**********'
NWORDS = []


def visit_dir(path):
    '''文件读取'''
    if not os.path.isdir(path):
        print("ERROR")
        return
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            all_file.append(os.path.join(root, f)[len(path)+1:])


def load_dic():
    global NWORDS
    '''字典读取'''
    f = open(dictionary, 'r')
    NWORDS = train(words(f.read()))
    for line in f:
        nlen = len(line)-1
        word_list.append(line[:nlen])
    f.close()


def divide_str(note, wordlist):
    '''连续字符串划分如iloveyou划分为 i love you'''
    i = 10
    head = 0
    flag = 0
    while head <= len(note) - 1:
        if head >= (len(note)-i):
            i = len(note)-head
        for p in range(i):
            rear = head + i - p
            flag = 0
            for each in wordlist:
                if note[head:rear] == each:
                    get_list.append(each)
                    head = head + len(each)
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            head = head + 1


def fuzzy_finder_by_interval(key, name_list):
    '''根据字典序和输入排序的模糊搜索'''
    key = key.strip()
    findings = []
    pattern = '.*?'.join(key)
    regex = re.compile(pattern)
    for item in name_list:
        match = regex.search(item)
        if match:
            findings.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(findings)]


def words(text): return re.findall('[a-z]+', text.lower())


def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words): return set(w for w in words if w in NWORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

def main():
    '''
    修改提交
    '''
    load_dic()
    visit_dir(file_path)
    tokenizer = TreebankWordTokenizer()
    my_input = input("请输入文件名称：")
    
        if ' ' not in my_input:
        divide_str(my_input, word_list)
        my_input = get_list
    else:
        my_input = tokenizer.tokenize(my_input)
        print(my_input)
        for i in range(len(my_input)):
            my_input[i] = correct(my_input[i])

    print(my_input)

  

    for i in range(len(my_input)):
        temp = fuzzy_finder_by_interval(my_input[i], all_file)
        for j in range(len(temp)):
            if temp[j] not in outcome:
                outcome.append(temp[j])
    print(outcome)
if __name__=='__main__':
    main()
