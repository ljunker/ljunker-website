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
        const formatterDate = new Intl.DateTimeFormat('de-DE', {
            day: 'numeric',
            month: 'short',
            year: 'numeric',
        });
        const formatterTime = new Intl.DateTimeFormat('de-DE', {
            timeZone: "Europe/Berlin",
            hour: "2-digit",
            minute: "2-digit",
            hourCycle: "h23"
        })
        filteredEvents.forEach(event => {
            var calEntry = icsFormatter();
            const dateTimeString = `${event.date}T${event.time}:00Z`;
            var begin = new Date(dateTimeString);
            var end = new Date(begin.getTime() + 120*60000);
            calEntry.addEvent(event.details, "", event.location, begin.toUTCString(), end.toUTCString());

            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${formatterDate.format(begin)}</td>
                <td>${formatterTime.format(begin)}</td>
                <td>${event.details}</td>
                <td>${event.location}</td>
                <td><button class="cal-download-btn">Zum Kalender hinzufügen</button></td>
            `;
            const button = row.querySelector(".cal-download-btn");
            button.addEventListener("click", () => {
                window.open(calEntry.download());
            });
            eventsBody.appendChild(row);
        });
    } else {
        noEventsMessage.style.display = 'block';
    }
}

setTimeout(function (){
    loadEvents();
}, 150);