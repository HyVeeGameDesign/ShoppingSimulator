using UnityEngine;

public class ItemController : MonoBehaviour
{
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            // Add logic to collect the item (e.g., add to inventory)
            // Update UI to reflect collected item
            Destroy(gameObject); // Remove the item from the scene
        }
    }
}
