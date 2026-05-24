class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mapping = new HashMap<>();

        for (int i =0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if(mapping.containsKey(diff)){
                return new int[] {mapping.get(diff), i};
            }

            mapping.put(num,i);
        }

        return new int[]{};
    }
}
