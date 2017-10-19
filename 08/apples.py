#start and end of house
house_left, house_right = input().strip().split(' ')
house_left, house_right = [int(house_left), int(house_right)]
#x_cor of apple and orange trees
apple_tree, orange_tree = input().strip().split(' ')
apple_tree, orange_tree = [int(apple_tree), int(orange_tree)]
#num of apples and oranges
num_apples, num_oranges = input().strip().split(' ')
num_apples, num_oranges = [int(num_apples), int(num_oranges)]
#distance of falling apples and oranges from resp. trees
apple_fall_loc = [int(apple) for apple in input().strip().split(' ')]
orange_fall_loc = [int(orange) for orange in input().strip().split(' ')]


#output:
#apples on house, oranges on house

def apples_output():
    ans = 0
    for app in apple_fall_loc:
        x_cor = apple_tree + app
        if x_cor >= house_left and x_cor <= house_right:
            ans += 1
    return ans

def oranges_output():
    ans = 0
    for oran in orange_fall_loc:
        x_cor = orange_tree + oran
        if x_cor >= house_left and x_cor <= house_right:
            ans += 1
    return ans

print ("Apples within house region: " + str(apples_output()))
print ("Oranges within house region: " + str(oranges_output()))