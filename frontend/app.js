/*
 * MumCare Frontend Controller
 *
 * Handles dashboard interactions and prepares communication
 * with the MumCare backend API.
 */

const API_BASE_URL = "http://localhost:8000";


/* ================= MODULES ================= */

function openModule(module) {
    const modal = document.getElementById("moduleModal");
    const content = document.getElementById("modalContent");

    const modules = {

        symptoms: {
            title: "Symptom Guidance",
            text:
                "Describe what you are experiencing and MumCare will provide an advisory risk category."
        },

        mood: {
            title: "Mood Check-in",
            text:
                "Tell MumCare how you are feeling today. Your emotional well-being matters."
        },

        documents: {
            title: "Health Documents",
            text:
                "This module will allow mothers to organize reports, prescriptions and test results."
        },

        reminders: {
            title: "Care Reminders",
            text:
                "This module will help manage medicines, appointments and important healthcare activities."
        }
    };

    const selected = modules[module];

    if (!selected) {
        return;
    }

    content.innerHTML = `
        <p class="eyebrow">MUMCARE MODULE</p>
        <h2>${selected.title}</h2>
        <p style="margin-top: 12px; line-height: 1.7; color: #777181;">
            ${selected.text}
        </p>
    `;

    modal.classList.remove("hidden");
}


function closeModule() {
    document
        .getElementById("moduleModal")
        .classList.add("hidden");
}


/* Close modal when clicking outside the card */

document
    .getElementById("moduleModal")
    .addEventListener("click", function (event) {

        if (event.target === this) {
            closeModule();
        }

    });


/* ================= AI ASSISTANT ================= */

async function sendAssistantMessage() {

    const input = document.getElementById("assistantInput");
    const responseBox = document.getElementById("assistantResponse");

    const message = input.value.trim();

    if (!message) {
        responseBox.textContent =
            "Please tell MumCare what you would like help with.";
        responseBox.classList.remove("hidden");
        return;
    }

    responseBox.textContent = "MumCare is analyzing your message...";
    responseBox.classList.remove("hidden");

    try {

        const response = await fetch(
            `${API_BASE_URL}/api/v1/symptoms/assess`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    symptom: message
                })
            }
        );

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        responseBox.innerHTML = `
            <strong>
                Guidance level: ${formatRiskLevel(data.risk_level)}
            </strong>

            <p style="margin-top: 8px;">
                ${data.guidance}
            </p>
        `;

    } catch (error) {

        /*
         * The interface remains usable even when the
         * backend is not running.
         */

        responseBox.innerHTML = `
            <strong>MumCare is currently in offline mode.</strong>

            <p style="margin-top: 8px;">
                The care interface is available, but the intelligence
                service is not connected right now.
            </p>
        `;
    }
}


/* ================= HELPERS ================= */

function formatRiskLevel(level) {

    if (!level) {
        return "Unknown";
    }

    return level.charAt(0).toUpperCase() + level.slice(1);
}


/* ================= KEYBOARD SUPPORT ================= */

document
    .getElementById("assistantInput")
    .addEventListener("keydown", function (event) {

        if (event.key === "Enter") {
            sendAssistantMessage();
        }

    });
