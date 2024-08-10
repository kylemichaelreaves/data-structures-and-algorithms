class Node
    attr_accessor :val, :prev, :next

    def initialize(val = nil, prev = nil, next_ = nil)
      @val = val
      @prev = prev
      @next = next_
    end
  end