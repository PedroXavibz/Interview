print("=============[ Sequência FIBONACCI ]=============\n")
number = int(input("Digite um número: "))


def fibonacci(target, current=0, next=1, repr_fib=""):
    repr_fib += f"{next} "

    if target == 0 or target == 1:
        print(f"Sequência: {current} {next}")
        return True

    sum = current + next

    current = next
    next = sum

    if sum == target:
        print(f" ・Sequência: 0 {repr_fib}{next}")
        return True
    elif sum > target:
        print(f" ・Sequência: 0 {repr_fib}{next}")
        return False
    return fibonacci(target, current, next, repr_fib)


print(f' ・Pertence a sequência? {"Sim" if fibonacci(number, 0, 1) else "Não"}.')
