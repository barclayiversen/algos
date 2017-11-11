function Node(data) {
  this.data = data;
  this.next = null;
}

function SLL(){
  this.head = null;
}

function length(head) {
    var count = 0;
    if(!head){
        return count;
    }
    else {
        var current = head;
        while (current.next) {
            current = current.next;
            count += 1
        }
    }
    return count + 1;
}

function count (head, data) {
    var counted = 0;
    var current;
    if(!head){
        return counted;
    } else {
        current = head;
        while (current != null) {
            if(current.data === data) {
                counted += 1;
                current = current.next;
            } else {
                current = current.next;
            }
        }
        return counted
    }
}