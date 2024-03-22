for i in range(1, 10):
    if i == 7:
        print("Reached", i, "breaking outer loop")
        break
    if i == 3:
        print("skipping", i, "in inner loop" )
        continue
    for y in range (1, 4):
        continue
    print(i)


    
    

        
