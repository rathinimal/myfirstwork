object HelloWorld {
  def main(args: Array[String]): Unit = {
    def maximum(a:Int,b:Int): Int = a>=b match{
      case true => a
      case false => b
      }
    print(maximum(3,12))
  }
}
