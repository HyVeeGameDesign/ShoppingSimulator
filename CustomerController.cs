using UnityEngine;

public class CustomerController : MonoBehaviour
{
    public string[] questions = { "Where are the restrooms?", "How much is this item?", "Do you have gluten-free bread?" };

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            // Randomly select a question
            string question = questions[Random.Range(0, questions.Length)];
            
            // Example: Display question in console
            Debug.Log("Customer asks: " + question);
        }
    }
}
