    const cards = document.querySelectorAll('.card');

    let hasFlippedCard = false;
    let lock = false;
    let first, second;
    let flips = 0;
    let time = 100;

    function flipCard(){
        if(lock) return;
        if(this === first) return;
        this.classList.add('flip');
        flips++;
        time--;
        document.getElementById('flips').innerHTML = flips;
        document.getElementById('time-remaining').innerHTML = time;
        if(!hasFlippedCard){
            hasFlippedCard = true;
            first = this;
            return;
        }
        second = this;
        checkMatch();
    }

    function checkMatch(){
        let isMatch = first.dataset.framework === second.dataset.framework;
        isMatch ? lockCards() : unflipCard(); 
    }

    function lockCards(){
        first.removeEventListener('click', flipCard);
        second.removeEventListener('click', flipCard);
        reset();
    }

    function unflipCard(){
        lock = true;
        setTimeout(() => {
            first.classList.remove('flip');
            second.classList.remove('flip');
            reset();
        }, 1500);
    }

    function reset(){
        [hasFlippedCard, lock] = [false,false];
        [first, second] = [null, null];
    }

    (function shuffle(){
        cards.forEach(card => {
            let pos = Math.floor(Math.random() * 4);
            card.style.order = pos;

        });

    })();
        cards.forEach(card=> card.addEventListener('click', flipCard));
