def test_one():
    print(">>> I'am test one")

def test_two(n):
    def test_tree(x):
        return x + n
    return test_tree

