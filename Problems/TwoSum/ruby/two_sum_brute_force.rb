"Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."

def two_sum(nums, target)
  nums.each_with_index do |num, i|
    (i + 1...nums.length).each do |j|
      if nums[j] == target - num
        return [i, j]
      end
    end
  end
end