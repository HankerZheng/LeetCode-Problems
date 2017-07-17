/*
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

Subscribe to see which companies asked this question
*/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */



//use the binary tree to solve the problem to obtain O(n) solution
//leaves count elements have been added to the tree struct 
struct b_tree
{
	int node;
	int smaller_count;
	int left_leaf_count;	//count the left leaves attached to this tree
	int right_leaf_count;	//count the right leaves attached to this tree
	struct b_tree *left;	//smaller than node
	struct b_tree *right;	//larger than or equal to node
};



 int* countSmaller(int* nums, int numsSize, int* returnSize) {
 	int* result;
	int i,j;
	int count;
	int flag;
	struct b_tree *head;
	struct b_tree *create;
	struct b_tree *temp1, *temp2;


	if(numsSize == 0)
	{
		*returnSize = 0;
		return NULL;
	}

	result = (int*) malloc(sizeof(int) * numsSize);
	memset(result, 0, sizeof(int) * numsSize/sizeof(char));

	//create the tree

	head = (struct b_tree*)malloc(sizeof(struct b_tree) * numsSize);
	memset(head, 0, sizeof(struct b_tree) * numsSize/sizeof(char));

	//from back to front
	for(i = numsSize-1; i >= 0; i--)
	{
		create = &head[i];

		create -> node = nums[i];
		create -> smaller_count = 0;
		create -> right_leaf_count = 0;
		create -> left_leaf_count = 0;
		create -> left = NULL;
		create -> right = NULL;

        if(i == numsSize-1)
            continue;

        count = 0;
		for(temp1 = &head[numsSize-1], temp2 =  &head[numsSize-1]; temp2 != NULL;)
		{
			temp1 = temp2;
			if( (create -> node) > (temp1 -> node) )
			{
				//self node and all node in the left should be increased;
				count += (1 + temp1->left_leaf_count);
				temp2 = temp1 -> right;
				temp1->right_leaf_count++;
			}
			else
			{
				temp2 = temp1 -> left;
				temp1->left_leaf_count++;
			}
		}

		if(create -> node > temp1 -> node)
			temp1->right = create;
		else
			temp1->left = create;

		create -> smaller_count = count;
	}

	for(i = 0; i< numsSize; i++)
	{
		result[i] = head[i].smaller_count;
	}

	free(head);

	*returnSize = numsSize;
	return result;

 }



//====================================================================================================
//			the solution below exceeds the time limit!! O(n^2)
//====================================================================================================
int* countSmaller(int* nums, int numsSize, int* returnSize) {

	int* result;
	int i,j;
	int count;

	if(numsSize == 0)
	{
		*returnSize = 0;
		return NULL;
	}

	result = (int*) malloc(sizeof(int) * numsSize);
	memset(result, 0, sizeof(int) * numsSize/sizeof(char));


	for(i = numsSize-1; i >= 0; i--)
	{
		count = 0;
		for(j = i+1; j< numsSize; j++)
		{
			if( nums[j] < nums[i])
				count++;
		}
		result[i] = count;
	}

	*returnSize = numsSize;
	return result;
    
}