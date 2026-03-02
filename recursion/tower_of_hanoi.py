def hanoi(n, source,helper, destination):
    if n == 1:
        return
    
    hanoi(n-1, source, destination, helper)

    hanoi(n-1, helper, source, destination)

hanoi(2, 'A', 'B', 'C')

    
    