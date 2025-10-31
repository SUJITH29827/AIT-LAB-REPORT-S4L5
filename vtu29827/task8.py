def solve_n_queens(n):
    solutions=[]
    cols=set()
    pos=set()
    neg=set()
    board=[-1]*n
    def backtrack(r):
        if r==n:
            sol=[]
            for i in range(n):
                row=['.']*n
                row[board[i]]='Q'
                sol.append(''.join(row))
            solutions.append(sol)
            return
        for c in range(n):
            if c in cols or (r+c) in pos or (r-c) in neg:
                continue
            cols.add(c); pos.add(r+c); neg.add(r-c); board[r]=c
            backtrack(r+1)
            cols.remove(c); pos.remove(r+c); neg.remove(r-c); board[r]=-1
    backtrack(0)
    return solutions

if __name__=="__main__":
    n=8
    sols=solve_n_queens(n)
    print(f"Total solutions for n={n}: {len(sols)}")
    for s in sols:
        for row in s:
            print(row)
        print()
