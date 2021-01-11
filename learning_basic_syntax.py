"""
1. 変数の使い方
"""
name1 = '竈門禰豆子'
name2 = '我妻善逸'
print('「{n1}」と「{n2}」は仲間です'.format(n1=name1, n2=name2))


"""
２ if文の使い方
"""
name2 = '鬼舞辻無惨'
if name2 == '鬼舞辻無惨':
    print('{}は仲間ではありません'.format(name2))
else:
    print('「{n1}」と「{n2}」は仲間です'.format(n1=name1, n2=name2))


"""
３ 配列の使い方
"""
name = ["竈門炭治郎", "冨岡義勇", "竈門禰豆子", "鬼舞辻無惨"]
name.append("我妻善逸")


"""
４ for文の使い方
"""
for character in name:
    print(character)


"""
５ 関数の使い方
"""


def print_name(member1, member2):
    if member2 == '鬼舞辻無惨':
        print('{}は仲間ではありません'.format(member2))
    else:
        print('「{m1}」と「{m2}」は仲間です'.format(m1=member1, m2=member2))


print_name('竈門禰豆子', '我妻善逸')
print_name('竈門禰豆子', '鬼舞辻無惨')


def print_name_list(name_list: list, *args):
    if args:
        for added_name in args:
            name_list.append(added_name)

    for character_name in name_list:
        print(character_name)


print_name_list(name, '煉獄杏寿郎', '胡蝶しのぶ')


"""
６ 引数を使う関数の使い方
"""


def check_favorite_name(favorite_name: str):

    if favorite_name in name:
        print('{}は含まれます'.format(favorite_name))


check_favorite_name('冨岡義勇')
