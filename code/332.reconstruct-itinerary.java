import java.util.List;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=332 lang=java
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
class Solution {
    // class Node {
    //     public String name;
    //     public PriorityQueue<String> to;

    //     public Node(String n) {
    //         this.name = n;
    //         to = new PriorityQueue<String>();
    //     }
    //     public void addTo(String t) {
    //         to.add(t);
    //     }
    // }

    // public HashMap<String, Node> graph = new HashMap<String, Node>();
    // public List<String> findItinerary(List<List<String>> tickets) {
    //     for(List<String> ticket: tickets) {
    //         String from = ticket.get(0);
    //         String to = ticket.get(1);
    //         if(!graph.containsKey(from)) {
    //             Node newNode = new Node(from);
    //             newNode.addTo(to);
    //             graph.put(from, newNode);
    //         }
    //         else {
    //             graph.get(from).addTo(to);
    //         }
    //     }
    //     List<String> ret = DFS(graph.get("JFK"), tickets.size());
    //     ret.add(0, "JFK");
    //     return ret;
    // }

    // public List<String> DFS(Node curr, int count) {
    //     List<String> ret;
    //     if(curr == null || curr.to.isEmpty()) {
    //         if(count == 0) {
    //             ret = new LinkedList<String>();
    //             return ret;
    //         }
    //         else {
    //             return null;
    //         }
    //     }

        
    //     String to = curr.to.poll();
    //     Node next = graph.get(to);
    //     ret = DFS(next, count-1);
    //     while(ret == null && !curr.to.isEmpty()) {
    //         String temp = to;
    //         to = curr.to.poll();
    //         next = graph.get(to);
    //         curr.addTo(temp);
    //         ret = DFS(next, count-1);
    //         if(ret == null && curr.to.isEmpty()) {
    //             curr.addTo(to);
    //             return null;
    //         }
    //     }
    //     if(ret == null) {
    //         curr.addTo(to);
    //         return null;
    //     }
    //     else {
    //         ret.add(0, to);
    //     }
    //     return ret;
    // }
    public List<String> findItinerary(List<List<String>> tickets) {
        LinkedList<String> ret = new LinkedList<String>();
        Map<String, PriorityQueue<String>> map = new HashMap<String, PriorityQueue<String>>();
        Stack<String> stack = new Stack<String>();
        for(List<String> t : tickets) {
            if(!map.containsKey(t.get(0))) map.put(t.get(0), new PriorityQueue<String>());
            map.get(t.get(0)).offer(t.get(1));
        }
        stack.push("JFK");
        while(!stack.isEmpty()) {
            String next = stack.peek();
            if(map.containsKey(next) && map.get(next).size() > 0) stack.push(map.get(next).poll());
            else ret.addFirst(stack.pop());
        }
        return ret;
    }
}


// @lc code=end

