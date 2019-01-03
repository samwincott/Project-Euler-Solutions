"""
This solves problem 8 of the project euler problems.
Found at https://projecteuler.net/problem=8
"""

def main():
    """
    Finds the thirteen adjacent digits with the greatest product,
    and prints the product.
    """
    thousand_digit_number = ("73167176531330624919225119674426574742355349194934969"
                             "83520312774506326239578318016984801869478851843858615"
                             "60789112949495459501737958331952853208805511125406987"
                             "47158523863050715693290963295227443043557668966489504"
                             "45244523161731856403098711121722383113622298934233803"
                             "08135336276614282806444486645238749303589072962904915"
                             "60440772390713810515859307960866701724271218839987979"
                             "08792274921901699720888093776657273330010533678812202"
                             "35421809751254540594752243525849077116705560136048395"
                             "86446706324415722155397536978179778461740649551492908"
                             "62569321978468622482839722413756570560574902614079729"
                             "68652414535100474821663704844031998900088952434506585"
                             "41227588666881164271714799244429282308634656748139191"
                             "23162824586178664583591245665294765456828489128831426"
                             "07690042242190226710556263211111093705442175069416589"
                             "60408071984038509624554443629812309878799272442849091"
                             "88845801561660979191338754992005240636899125607176060"
                             "58861164671094050775410022569831552000559357297257163"
                             "6269561882670428252483600823257530420752963450")

    product = 0

    thousand_digit_number = thousand_digit_number.replace("\n", "")

    for i in range(0, len(thousand_digit_number) - 12):
        temp_product = 1
        for j in range(i, i + 13):
            temp_product *= int(thousand_digit_number[j])
        if temp_product >= product:
            product = temp_product

    print("The answer is", product)

main()
