import gleam/list
import gleam/string
import exercism/test_runner.{debug}
pub fn recite(inputs: List(String)) -> String { 
  case inputs {
    [wanted, ..] -> inputs 
      |> list.window_by_2
      |> list.map(fn (pair) {
        "For want of a " <> pair.0 <> " the " <> pair.1 <> " was lost.\n"
      })
      |> string.join("") 
      <> "And all for the want of a " <> wanted <> "."
    [] -> ""
  }
}
