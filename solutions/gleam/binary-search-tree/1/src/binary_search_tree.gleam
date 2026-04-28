import gleam/list

pub type Tree {
  Nil
  Node(data: Int, left: Tree, right: Tree)
}

pub fn to_tree(data: List(Int)) -> Tree {
  data |> list.fold(Nil, insert)
}

fn insert(tree: Tree, item: Int) -> Tree {
  case tree {
    Nil -> Node(item, Nil, Nil)
    Node(data:, left:, right:) if data >= item ->
      Node(data, insert(left, item), right)
    Node(data:, left:, right:) -> Node(data, left, insert(right, item))
  }
}

fn to_list(tree: Tree) -> List(Int) {
  case tree {
    Nil -> []
    Node(data:, left:, right:) -> {
      let left = to_list(left)
      let right = to_list(right)
      list.append(left, [data, ..right])
    }
  }
}

pub fn sorted_data(data: List(Int)) -> List(Int) {
  data |> to_tree |> to_list
}
