# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 01:31:59 2019

@author: Administrator
"""

class DoubleDimensionNode():
    
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
    
class DoubleDimensionLinlist():
    
    def __init__(self,node=None):
        self.head=node
        self.end=node
        
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def length(self):
        cur=self.head
        count=0
        while cur!=None:
            count+=1;
            cur=cur.next
        return count
    
    def travel(self):
        
        cur=self.head
        while cur!=None:
            print(cur.data,end=' ')
            cur=cur.next
        print()
        
    def add(self,data):
        
        node=DoubleDimensionNode(data)
        if self.head!=None:
            node.next=self.head
            self.head=node#self.head要更新
            self.head.next.pre=node
        else:
            self.head=node
            self.end=node
            
            
            
    def append(self,data):
        node=DoubleDimensionNode(data)
        if self.head==None:
            self.head=node
            self.end=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur
            node.next=None
            self.end=node
            
    def insert(self,pos,data):
        if pos<=0:
            self.add(data)
        elif pos>=(self.length()):
            self.append(data)
        else:
            node=DoubleDimensionNode(data)
            if pos<=int(0.5*(self.length())):
                count=0
                cur=self.head
               #nex=None
                while count<(pos-1):
                    cur=cur.next
                    
                    count+=1
                node.pre=cur
                node.next=cur.next
                cur.next.pre=node
                cur.next=node
            else:
                count=int(self.length())
                cur=self.end
                pr=None
                while count>(pos+1):
                    cur=cur.pre
                    pr=cur.pre
                    count-=1
                cur.pre=node
                node.pre=pr
                node.next=cur
                pr.next=node
    
    def search(self,data):
        cur=self.head
        while cur!=None:
            if cur.data==data:
                return True
            else:
                cur=cur.next
        return False
    
    def check(self,pos):
        if pos<=0:
            return
        elif pos>=(self.length()+1):
            return
        elif pos<=int(0.5*(self.length())):
            count=0
            cur=self.head
            while count!=pos:
                count+=1
                cur=cur.next
            print(cur.data,end=' ')
        else:
            count=int(self.length())
            cur=self.end
            while count!=pos:
                count-=1
                cur=cur.pre
            print(cur.data,end=' ')
    
    def remove(self,data):
        if (self.is_empty())or(not(self.search(data))):
            return
        prev=None
        cur=self.head
        count=0
        while count<=int(self.length()):
            if cur.data==data:
                if prev==None:
                    self.head=cur.next
                    self.head.pre=None
                elif cur.next==None:
                    self.end=cur.pre
                    self.end.next=None
                else:
                    prev.next=cur.next
                    cur.next.pre=prev
            count+=1
            prev=cur
            cur=cur.next
        
        #while cur!=None:
            
            #if cur.data!=data:
                #pre=cur
                #cur=cur.next
            #else:
                #if cur==self.head:
                    #self.head=cur.next
                    #self.head.pre=None
                    #break
                #elif cur==self.end:
                    #self.end=cur.pre
                    #self.end.next=None
                    #break
                #else:
                    #pre.next=cur.next
                    #cur.next.pre=pre
                    #break
    
    def delete(self,pos):
        length=int(self.length())
        if (pos<=0)or(pos>int(length)):
            return
        if length>1:
            if pos<=int(0.5*length):
                count=1
                prev=None
                cur=self.head
                while count<pos:
                    prev=cur
                    cur=cur.next
                    count+=1
                if prev==None:
                    self.head=cur.next
                    self.head.pre=None
                else:
                    prev.next=cur.next
                    cur.next.pre=prev
            if pos>int(0.5*length):
                count=length
                cur=self.end
                nex=None
                while count>pos:
                    nex=cur
                    cur=cur.pre
                    count-=1
                if nex==None:
                    self.end=cur.pre
                    self.end.next=None
                else:
                    nex.pre=cur.pre
                    cur.pre.next=nex
        return
            
        
        #elif pos<=int(0.5*length):
            #count=0
            #cur=self.head
            #pre=None
            #while count!=pos:
                #count+=1
                #pre=cur
                #cur=cur.next
            #pre.next=cur.next
            #cur.next.next=pre
            
        #else:
            #count=length
            #cur=self.end
            #nex=None
            #while count!=pos:
                #count-=1
                #nex=cur
                #cur=cur.pre
            #nex.pre=cur.pre
            #cur.pre.next=nex
           
    
                    
        
                
            
        
        