const interviewQuestions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Describe a challenging project you worked on and how you overcame obstacles.",
    "How do you handle stress and pressure?",
    // Add more interview questions here
];

const getRandomQuestion = () => {
    const randomIndex = Math.floor(Math.random() * interviewQuestions.length);
    return interviewQuestions[randomIndex];
};

const displayQuestion = () => {
    const question = getRandomQuestion();
    const interviewQuestionElement = document.getElementById("interviewQuestion");
    interviewQuestionElement.textContent = question;
};

const evaluateAnswer = (answer) => {
    // Simulated AI evaluation - replace with actual AI logic
    const feedback = (Math.random() < 0.5) ? "Your answer was clear and well-structured. Great job!" : "You could provide more specific examples to support your points. Consider elaborating further.";
    return feedback;
};

document.addEventListener("DOMContentLoaded", () => {
    displayQuestion();

    const submitButton = document.getElementById("submitAnswer");
    submitButton.addEventListener("click", () => {
        const answer = document.getElementById("answer").value.trim();
        if (answer !== "") {
            const feedback = evaluateAnswer(answer);
            const feedbackElement = document.getElementById("feedback");
            feedbackElement.textContent = feedback;
        }
    });
});
