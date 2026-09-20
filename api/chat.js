export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Méthode non autorisée. Utilisez POST.' });
  }

  // La clé de l'API Groq (Llama 3)
  const apiKey = process.env.GROQ_API_KEY;

  if (!apiKey) {
    return res.status(500).json({ error: 'La clé API GROQ_API_KEY n\'est pas configurée dans Vercel.' });
  }

  const userMessage = req.body.message;
  if (!userMessage) {
    return res.status(400).json({ error: 'Le message est vide.' });
  }

  const url = 'https://api.groq.com/openai/v1/chat/completions';

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: "openai/gpt-oss-120b", // Modèle demandé par l'utilisateur
        messages: [
          {
            role: "system",
            content: "Tu es un expert réseau Cisco CCNA. Ton but est d'aider les étudiants marocains. Réponds de manière très concise, amicale et pédagogique. Tu peux utiliser un peu de darija si besoin."
          },
          {
            role: "user",
            content: userMessage
          }
        ]
      })
    });

    const data = await response.json();

    if (data.error) {
      return res.status(500).json({ error: data.error.message });
    }

    const reply = data.choices[0].message.content;
    return res.status(200).json({ reply });
    
  } catch (error) {
    return res.status(500).json({ error: "Erreur lors de la communication avec l'API Groq." });
  }
}
