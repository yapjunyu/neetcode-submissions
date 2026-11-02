class Solution {
    public int[] twoSum(int[] nums, int target) {
        // create hashmap of number: index, return index if remainder == number
        HashMap<Integer, Integer> hmap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remainder = target - nums[i];
            if (hmap.containsKey(remainder)) {
                return new int[]{hmap.get(remainder), i};
            }
            hmap.put(nums[i], i);
        }
        return new int[0];
    }
}
