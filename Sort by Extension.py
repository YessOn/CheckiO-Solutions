from typing import List
def sort_by_ext(files: List[str]) -> List[str]:
    dots_sorted = sorted([i for i in files if ((i.startswith('.') and len(i.split(".")) <= 2) or i.endswith('.'))])
	for j in sorted([i.split(".")[::-1] for i in [i for i in files if not ((i.startswith('.') and len(i.split(".")) <= 2) or i.endswith('.'))]]):
		ext_sorted = ['.'.join(j[::-1]) for j in sorted([i.split(".")[::-1] for i in [i for i in files if not ((i.startswith('.') and len(i.split(".")) <= 2) or i.endswith('.'))]])]
	return dots_sorted + ext_sorted
    #Using OS library which is Forbidden On CheckiO
    #import os.path as pt
    #return sorted(files,key=lambda x: pt.splitext(x)[1])

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
