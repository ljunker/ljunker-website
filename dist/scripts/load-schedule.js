async function loadEvents() {
    const response = await fetch('events.json');
    const events = await response.json();
    const today = new Date();
    today.setDate(today.getDate()-1);
    const twoWeeksLater = new Date();
    twoWeeksLater.setDate(today.getDate() + 31);

    const filteredEvents = events.filter(event => {
        const eventDate = new Date(event.date);
        return eventDate >= today && eventDate <= twoWeeksLater;
    })
    .sort((a, b) => new Date(a.date) - new Date(b.date));

    const eventsBody = document.getElementById('events-body');
    const noEventsMessage = document.getElementById('no-events');

    if (filteredEvents.length > 0) {
        noEventsMessage.style.display = 'none';
        const formatter = new Intl.DateTimeFormat('de-DE', {
            day: 'numeric',
            month: 'short',
            year: 'numeric',
        });
        filteredEvents.forEach(event => {
            const eventDate = new Date(event.date);
            const formattedDate = formatter.format(eventDate);
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${formattedDate}</td>
                <td>${event.time}</td>
                <td>${event.details}</td>
                <td>${event.location}</td>
            `;
            eventsBody.appendChild(row);
        });
    } else {
        noEventsMessage.style.display = 'block';
    }
}

setTimeout(function (){
    loadEvents();
}, 150);