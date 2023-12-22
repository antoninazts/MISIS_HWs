// Решение задачи https://rosettacode.org/wiki/Teacup_rim_text#AWK

import scala.io.Source
object Teacup_rim_text {
  def main(args: Array[String]): Unit = {
    val source = Source.fromFile(".\\unixdict.txt")
    val unixdict = source.getLines().filter(_.matches("[A-Za-z]{3,}")).filterNot(_.matches("^(\\w)\\1\\1$")).toList
    source.close()
    var stop_duplicates: List[String] = Nil
    for (word <- 0 until unixdict.length) {
      val origin_word = unixdict(word)
      if (!stop_duplicates.contains(origin_word)) then {
        var sub_list: List[String] = Nil
        for (i <- 0 until origin_word.length) {
          val trans_word = origin_word.substring(i) + origin_word.substring(0, i)
          sub_list = trans_word :: sub_list
          stop_duplicates = trans_word :: stop_duplicates
        }
        if sub_list.forall(unixdict.contains) then println(sub_list mkString " -> ")
      }
    }
  }
}
