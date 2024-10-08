#!/usr/bin/env python3
#  Jeff Bohn
#  10/1/2024
#  Recursion and Algorithms
#  Chapter 13

############ Exercise 13-2 ############

# all discs start on the left peg, and only one disc gets moved per recursive function call

def move_disk(n, src, dest, temp):
    count = n
    if count >= 0:
        count = count - 1
        print(f"      move_disk(n={n}, src={src}, dest={dest}, temp={temp})")
        
    if n == 0:
        return
    else:
        move_disk(n-1, src, temp, dest)
        # print(f"      move_disk({n} from {src} to {dest})")
        move_disk(n-1, temp, dest, src)
        
def main():
    print("**** TOWERS OF HANOI ****\n")

    num_disks = int(input("Enter number of disks: "))
    print()
    move_disk(num_disks, "A", "C", "B")

    print()
    print("All disks have been moved.")


main()


# def move_disk(n):
#     print(f'print_1:  {n}')
#     if n == 0:
#         return
#     else:
#         one = move_disk(n-1)
#         print(f'print_one:  {one} n: {n}')
#       # two = move_disk(n-1)
#         # print(f'print_two:  {two} n: {n}')
          
        
# def main():

#     num_disks = int(input("Enter number of disks: "))
#     move_disk(num_disks)
#     print("All done.")

# main()

