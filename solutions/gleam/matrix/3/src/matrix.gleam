import gleam/int
import gleam/list
import gleam/result
import gleam/string

fn at(list: List(item), index: Int) -> Result(item, Nil) {
  list |> list.drop(index - 1) |> list.first
}

pub fn row(index: Int, string: String) -> Result(List(Int), Nil) {
  let rows = string.split(string, on: "\n")
  rows
  |> list.try_map(fn(row) {
    string.split(row, on: " ")
    |> list.try_map(int.parse)
  })
  |> result.try(at(_, index))
}

pub fn column(index: Int, string: String) -> Result(List(Int), Nil) {
  let rows = string.split(string, on: "\n")
  rows
  |> list.try_map(fn(row) {
    string.split(row, on: " ")
    |> list.try_map(int.parse)
    |> result.try(at(_, index))
  })
}
