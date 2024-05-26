def RightRotate(a, n, k):

    # If rotation is greater 
    # than size of array
    k = k % n;

    for i in range(0, n):

        if(i < k):

            # Printing rightmost 
            # kth elements
            print(a[n + i - k], end = " ");

        else:

            # Prints array after
            # 'k' elements
            print(a[i - k], end = " ");

    print("\n");

# Driver code
Array = [ 1, 2, 3, 4, 5 ];
N = len(Array);
K = 2;
    
RightRotate(Array, N, K);