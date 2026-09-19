export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Méthode non autorisée. Utilisez POST.' });
  }

  // The API key is stored securely in Vercel Environment Variables
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(500).json({ error: 'La clé API GEMINI_API_KEY n\'est pas configurée dans Vercel.' });
  }

  const userMessage = req.body.message;
  if (!userMessage) {
    return res.status(400).json({ error: 'Le message est vide.' });
  }

  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=${apiKey}`;

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        system_instruction: {
          parts: {
            text: "Tu es un expert réseau Cisco CCNA. Ton but est d'aider les étudiants marocains. Réponds de manière très concise, amicale et pédagogique. Tu peux utiliser un peu de darija si besoin."
          }
        },
        contents: [
          {
            parts: [{ text: userMessage }]
          }
        ]
      })
    });

    const data = await response.json();

    if (data.error) {
      return res.status(500).json({ error: data.error.message });
    }

    const reply = data.candidates[0].content.parts[0].text;
    return res.status(200).json({ reply });
    
  } catch (error) {
    return res.status(500).json({ error: "Erreur lors de la communication avec l'API Gemini." });
  }
}
