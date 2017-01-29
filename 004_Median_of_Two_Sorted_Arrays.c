/*There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).*/


struct array_elem
{
	int val;
	int index;
};

double range_shrink(int* nums1, int* nums2, struct array_elem *num0, struct array_elem *num1, struct array_elem *num2, struct array_elem *num3, int totalSize);
int is_int(int num1, int dividend);

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {

// array 1 [0...nums1Size-1];
// array 2 [0...nums2Size-1];

	struct array_elem range[4];
	struct array_elem temp;

	range[0].val = *nums1;
	range[0].index = 0;

	range[1].val = *(nums1+nums1Size-1);
	range[1].index = nums1Size-1;

	range[2].val = *nums2;
	range[2].index = 0;

	range[3].val = *(nums2+nums2Size-1);
	range[3].index = nums2Size-1;

	return range_shrink(nums1, nums2, &range[0], &range[1], &range[2], &range[3], nums1Size + nums2Size - 1);
}


//totalSize is m+n-1
double range_shrink(int* nums1, int* nums2, struct array_elem *num0, struct array_elem *num1, struct array_elem *num2, struct array_elem *num3, int totalSize)
{

	int mid_temp1;
	int mid_temp2;

	//base case: there is only 4 elements in the range
	if( (num0->index - num1->index <= 2)&&( num2->index - num3->index <= 2) )
	{
		num0->index = (num0->val < num2->val) ? (num2->index - 1 + num0->index):(num2->index + num0->index);
		num2->index = (num2->val < num0->val) ? (num0->index - 1 + num2->index):(num0->index + num2->index);

		if(num1->val > num3->val)
		{
			num1->index = num1->index + num3->index;
			if(num3->val < num0->val)
				num3->index = num0->index - 1 + num3->index;
			else
				num3->index = num0->index + num3->index;
		}
		else
		{
			num3->index = num1->index + num3->index;
			if(num1->val < num2->val)
				num1->index = num2->index - 1 + num1->index;
			else
				num1->index = num2->index + num1->index;
		}
		if(is_int(totalSize,2))
		{
			if(num0->index == totalSize/2)
				return num0->val;
			if(num1->index == totalSize/2)
				return num1->val;
			if(num2->index == totalSize/2)
				return num2->val;
			if(num3->index == totalSize/2)
				return (double)num3->val;
		}
		else
		{			
			if(num0->index == totalSize/2)
				mid_temp1 = num0->val;
			else if(num0->index == totalSize/2+1)
				mid_temp2 = num0->val;

			if(num1->index == totalSize/2)
				mid_temp1 = num1->val;
			else if(num1->index == totalSize/2+1)
				mid_temp2 = num1->val;

			if(num2->index == totalSize/2)
				mid_temp1 = num2->val;
			else if(num0->index == totalSize/2+1)
				mid_temp2 = num2->val;

			if(num3->index == totalSize/2)
				mid_temp1 = num3->val;
			else if(num0->index == totalSize/2+1)
				mid_temp2 = num3->val;

			return ((double)mid_temp1+(double)mid_temp2)/2;
		}
	}
	else
		return 0;
	//above is base case;

	

}

int is_int(int num, int dividend)
{
	if (num % dividend)
		return 0;
	else 
		return 1;
}

