 '''
 You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the  same night. Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example:
Input:​ nums = [1,2,3,1]
Output:​ 4
Input:​ nums = [2,7,9,3,1]
Output:​ 12
Input:​ nums = [2,7,9,3,10,5,4,6]
Output:​ 27


Solution:

This function accepts two parameters-
    List of House amount and total houses
        (Example here,
            hvalue = [2,7,9,3,10,5,4,6] and total_houses = 8
        )
'''

# calculate the maximum stolen amount 
def maximize_loot(hval, total_houses): 
	if total_houses == 0: 
		return 0
	if total_houses == 1: 
		return hval[0] 
	if total_houses == 2: 
		return max(hval[0], hval[1]) 

	# total_stolen_amt[i] represent the maximum amount stolen so 
	# for after reaching house i. 
	total_stolen_amt = [0]*total_houses 

	# Initializing the total_stolen_amt[0] and total_stolen_amt[1] 
	total_stolen_amt[0] = hval[0] 
	total_stolen_amt[1] = max(hval[0], hval[1]) 
	
	# Fill remaining positions 
	for i in range(2, total_houses): 
		total_stolen_amt[i] = max(hval[i]+total_stolen_amt[i-2], total_stolen_amt[i-1]) 
	return total_stolen_amt[-1] 


##Program execution starts from here
if __name__ == '__main__': 
    house_val = [2,7,9,3,10,5,4,6]
    total_houses = len(house_val)
    ##If we want dynamic values for 'house_val' & 'total_houses'
    ##we can replace above 2 lines by below    
    #total_houses = int(input("Enter the number of houses followed by its cost\nInput:\n"))
    #house_val = [int(input()) for i in range(0,n)]      
    print("Output: {}".format(maximize_loot(house_val, total_houses)))
