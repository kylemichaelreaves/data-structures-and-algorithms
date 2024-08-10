require 'Node.rb'

class SinglyLinkedList
    include Enumerable
    attr_accessor :head

    def initialize
      @head = nil
    end

    def insert_tail(value)
      newNode = Node.new(value)
      if @head.nil?
        @head = newNode
      else
        tempNode = @head
        tempNode = tempNode.next until tempNode.next.nil?
        tempNode.next = newNode
      end
    end

    def insert_head(value)
      newNode = Node.new(value)
      if @head.nil?
        @head = newNode
      else
        newNode.next = @head
        @head = newNode
      end
    end

    def each
      return if @head.nil?

      current = @head
      until current.nil?
        yield current.value
        current = current.next
      end
    end

    def print_list
      puts '[' + to_a.join(', ') + ']'
    end

    def delete_head
      if !@head.nil? && !@head.next.nil?
        newHead = @head.next
        @head = newHead
      elsif !@head.nil? && @head.next.nil?
        @head = nil
      end
    end

    def delete_tail
      return if @head.nil?

      tempNode = @head
      tempNode = tempNode.next until tempNode.next.next.nil?
      tempNode.next = nil
    end

    def empty?
      @head.nil?
    end
  end