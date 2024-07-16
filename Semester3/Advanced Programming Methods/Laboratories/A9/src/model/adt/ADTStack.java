package model.adt;

import java.util.*;

import exceptions.ADTException;

public class ADTStack<T> implements IADTStack<T> {
    private final Deque<T> deque;

    public ADTStack() {
        deque = new LinkedList<>();
    }

    @Override
    public T pop() throws ADTException {
        if (deque.isEmpty()) {
            throw new ADTException("Stack Error: Stack is empty.");
        }

        return deque.pop();
    }

    @Override
    public T peek() throws ADTException {
        if (deque.isEmpty()) {
            throw new ADTException("Stack Error: Stack is empty.");
        }

        return deque.peek();
    }

    @Override
    public void push(T v) {
        deque.push(v);
    }

    @Override
    public boolean isEmpty() {
        return deque.isEmpty();
    }

    @Override
    public Iterator<T> iterator() {
        return deque.iterator();
    }

    @Override
    public Deque<T> getStack() {
        return deque;
    }

    @Override
    public List<T> getReversed() {
        List<T> list = Arrays.asList((T[]) deque.toArray());
        Collections.reverse(list);
        return list;
    }
}
