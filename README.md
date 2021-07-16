# Minimax-search-algorithm
A program that uses minimax search algorithm on a tree that has 4 layer and 5 child node each layer. Written in Python.

# 1) Creation of Tree

I created the tree using a two dimensional array. First I created a two dimensional array with 4 elements. In the last element, there are 625 randomly generated scores between 0-1000. The remaining three are empty arrays. Then I fill in the empty elements of the array using the minimax function I wrote.

# 2) Minimax Algorithm

I sended the tree that I have created as I mentioned above to the function named Minimax as an argument. I traveled the array with the for loop starting from the leaves of the tree. In each traveling, I replaced the maximum or minimum (varies from layer to layer) of the scores that I have grouped five by five to one top layer (i.e. previos element of the array). Maximum value of first layer of the tree that I have filled in this way is result score and I return it.

# 3) Screenshot from Program

![image](https://user-images.githubusercontent.com/67736718/125965430-11b1853c-51b3-420f-837b-82f944a46993.png)

![image](https://user-images.githubusercontent.com/67736718/125965452-74eefc84-cc09-49d6-ab44-424c488295f1.png)
