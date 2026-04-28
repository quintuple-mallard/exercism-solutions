import gleam/int
import gleam/list
import gleam/result
import gleam/string

fn at(list: List(item), index: Int) -> Result(item, Nil) {
  case list {
    _ if index < 1 -> Error(Nil)
    [] -> Error(Nil)
    [fst, ..] if index == 1 -> Ok(fst)
    [_, ..rest] -> at(rest, index - 1)
  }
}

pub fn row(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> string.split(on: "\n")
  |> list.map(fn(row) {
    string.split(row, on: " ")
    |> list.map(int.parse)
    |> result.all
  })
  |> result.all
  |> result.try(at(_, index))
}

pub fn column(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> string.split(on: "\n")
  |> list.map(fn(row) {
    string.split(row, on: " ")
    |> list.map(int.parse)
    |> result.all
    |> result.try(at(_, index))
  })
  |> result.all
}
