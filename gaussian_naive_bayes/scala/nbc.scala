import org.saddle._

object Main {
  def main(args: Array[String]) {
    // Initialisation
    // target variable
    val gender: Series[Int, Any] = Series("male", "male", "male", "male", 
    "female", "female", "female", "female")
    
    // feature variables
    val height: Series[Int, Any] = Series(6.0, 5.92, 5.58, 5.92, 5.0, 5.5, 
    5.42, 5.75)
    val weight: Series[Int, Any] = Series(180, 190, 170, 165, 100, 150, 130, 150)
    val foot_size: Series[Int, Any] = Series(12, 11, 12, 10, 6, 8, 7, 9)
    val data = Frame("Gender" -> gender, "Height" -> height, "Weight" -> weight, 
    "Foot_Size" -> foot_size)

    // test data
    val person_height: Series[Int, Any] = Series(6.0)
    val person_weight: Series[Int, Any] = Series(130)
    val person_foot_size: Series[Int, Any] = Series(8)
    val person = Frame("Height" -> person_height, "Weight" -> person_weight, 
    "Foot_Size" -> person_foot_size)

    // Calculate Priors
    // number of males, females
    val n_male = data.colAt(0).filter(_ == "male").numRows
    val n_female = data.colAt(0).filter(_ == "female").numRows

    // // total rows
    val total_ppl = data.colAt(0).numRows

    // // prior is number of males divided by the total rows
    val p_male = n_male.toFloat / total_ppl

    // // prior is number of females divided by the total rows
    val p_female = n_female.toFloat / total_ppl

    println(p_female)
  }
}
