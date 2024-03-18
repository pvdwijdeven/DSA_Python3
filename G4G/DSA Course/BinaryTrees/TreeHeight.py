class Node:

  def __init__(self, val) -> None:
    self.data: int | float = val
    self.left: Node | None = None
    self.right: Node | None = None


def height(root):
  # code here
  return 0 if root is None else max(
      height(root.left) + 1,
      height(root.right) + 1)


if __name__ == "__main__":
  root = Node(1)
  root.left = Node(4)  # type: ignore
  root.left.left = Node(4)  # type: ignore
  root.left.right = Node(2)  # type: ignore

  print(height(root))
