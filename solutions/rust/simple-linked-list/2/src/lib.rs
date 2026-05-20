use std::mem;
#[derive(Debug, Clone)]
pub enum SimpleLinkedList<T> {
    Node(T, Box<SimpleLinkedList<T>>),
    End
}

impl<T: Clone> SimpleLinkedList<T> {
    pub fn new() -> Self {
        Self::End
    }

    // You may be wondering why it's necessary to have is_empty()
    // when it can easily be determined from len().
    // It's good custom to have both because len() can be expensive for some types,
    // whereas is_empty() is almost always cheap.
    // (Also ask yourself whether len() is expensive for SimpleLinkedList)
    pub fn is_empty(&self) -> bool {
        match self {
            Self::End => true,
            Self::Node(_, _) => false,
        }
    }

    pub fn len(&self) -> usize {
        let mut head = self.clone();
        let mut len = 0;
        while let SimpleLinkedList::Node(_, tail) = head {
            len += 1;
            head = *tail;
        }
        len
    }

    pub fn push(&mut self, element: T) {
        let head = mem::replace(self, Self::End);
        *self = Self::Node(element, Box::new(head));
    }

    pub fn pop(&mut self) -> Option<T> {
        let head = mem::replace(self, Self::End);
        match head {
            Self::End => None,
            Self::Node(val, next) => {
                *self = *next;
                Some(val)
            }
        }
    }

    pub fn peek(&self) -> Option<&T> {
        match self {
            Self::End => None,
            Self::Node(val, _) => Some(val),
        }
    }

    #[must_use]
    pub fn rev(self) -> SimpleLinkedList<T> {
        Vec::from(self).into_iter().rev().collect()
    }
}

impl<T: Clone> FromIterator<T> for SimpleLinkedList<T> {
    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
        let mut list = SimpleLinkedList::new();
        for item in iter {
            list.push(item);
        }
        list
    }
}

impl<T> From<SimpleLinkedList<T>> for Vec<T> {
    fn from(list: SimpleLinkedList<T>) -> Vec<T> {
        let mut next = Box::new(list);
        let mut vec = Vec::new();
        while let SimpleLinkedList::Node(val, tail) = *next {
            vec.push(val);
            next = tail;
        }
        vec.into_iter().rev().collect()
    }
}
