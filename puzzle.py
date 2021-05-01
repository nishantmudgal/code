
'''
Consider a simple puzzle represented by a string with characters (., #): It may look like this: puzzle = ‘...##..#’. Each ‘.’ character represents an open space, and each ‘#’ character represents an occupied space. A puzzle can have any size. Suppose you are given a set of puzzle pieces as a list of strings (ex. [‘##......’, ‘....##..’, ‘.......#’] is a list of three puzzle pieces). Each piece is represented by a string of the same size as the puzzle string. You can add a piece to the puzzle if for any index they both don’t have a ‘#’ character (For example, you can add ‘##......’ to ‘...##..#’ to get ‘##.##..#’). You have the option of adding any existing piece or the reverse of any existing piece: (For example if you have ‘##......’ you have the option to fit it as ‘......##’). The goal is to complete the puzzle by adding a subset of puzzle pieces. A completed puzzle is a string with all characters equal to ‘#’. (Example of a completed puzzle is ‘########’). Question: How would you design a recursive algorithm to solve the puzzle?

Example 1: Suppose that the initial puzzle looks like this: puzzle = ‘####..#.’. The puzzle pieces are: pieces= ['#.......', '.##.....', '....##..'] You can add the first piece flipped ( '.......#' ) to get puzzle_2 = ‘####..##’. Then you can add the third piece ( '....##..') to get puzzle_3 = ‘########’. Therefore you can complete the puzzle and your function should return True.

Example 2: Suppose that the initial puzzle looks like this: puzzle = ‘...’. And the puzzle pieces are: pieces= ['##.', '.##’ ] This puzzle has no solution: If you add the first piece then the puzzle looks like this '##.'. The second piece cannot fit

Example 3: Suppose that the initial puzzle looks like this: puzzle = ‘....’. And the puzzle pieces are: pieces= ['##..', '....’ ] This puzzle has no solution: Note that you can only use each piece once.
'''


# Function takes puzzle string and pieces list
# Return True if the puzzle can be completed using the pieces else False
def is_complete_puzzle(puzzle_str, pieces):

    # length of the puzzle string
    puzzle_len = len(puzzle_str)

    # Returns True if there is no '.' in the string i.e. string is complete
    def is_complete(puzzle):
        for i in range(puzzle_len):
            if puzzle[i] == '.':
                return False
        return True

    # Return the string after adding 2 input string. Parameter 'reversed_add' defines if the second string is to be added in reverse or not
    def add_two_string(str1, str2, reversed_add):
        res = list(str1)
        add_str = str2 if not reversed_add else str2[::-1]
        for i in range(puzzle_len):
            if add_str[i] == '#' and res[i] == '.':
                res[i] = '#'
        return "".join(res)

    # Implementation of the logic of recursion
    def solve_recursion(puzzle, index_current_piece):

        # Return true if the puzzle is completed
        if is_complete(puzzle):
            return True

        # Return False if all the pieces are tried
        if index_current_piece == len(pieces):
            return False

        # Return True if we get complete string using the current piece in normally or reversed
        return (solve_recursion(add_two_string(puzzle, pieces[index_current_piece-1], True), index_current_piece+1) or
                solve_recursion(add_two_string(puzzle, pieces[index_current_piece-1], False), index_current_piece+1))

    return solve_recursion(puzzle_str, 0)

# main function


def main():
    # puzzle string
    puzzle_str = "....##.#"
    # pieces list
    puzzle_pieces = ['##......', '....#...', '......#.']

    result = is_complete_puzzle(puzzle_str, puzzle_pieces)
    print(result)


if __name__ == "__main__":
    main()
