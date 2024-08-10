def rotate(nums, k)
  n = nums.length
  a = Array.new(n, 0)
  nums.each_with_index do |num, i|
    a[(i + k) % n] = num
  end

  nums.replace(a)
end