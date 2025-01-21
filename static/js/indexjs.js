       // Add chemistry animations
       function createAnimations() {
           const animationsContainer = document.getElementById('animations');
           const molecules = ['⚛️', '🧪', '🔬', '🧫'];
           
           // Create molecules
           for (let i = 0; i < 8; i++) {
               const molecule = document.createElement('div');
               molecule.className = 'molecule';
               molecule.textContent = molecules[Math.floor(Math.random() * molecules.length)];
               molecule.style.left = `${Math.random() * 100}vw`;
               molecule.style.animationDelay = `${Math.random() * 5}s`;
               
               animationsContainer.appendChild(molecule);
           }
       }

       // Initialize animations
       createAnimations();

       function fetchChapters() {
        const standardId = document.getElementById('standard').value;
        console.log("Selected Standard ID:", standardId);
     
        if (standardId) {
            fetch(`/get-chapters/?standard_id=${standardId}`)
                .then(response => response.json())
                .then(data => {
                    console.log("Chapters data:", data);
                    const chapterSelect = document.getElementById('chapter');
                    chapterSelect.innerHTML = '<option value="" disabled selected>Choose Chapter</option>';
                    for (const chapter of data.chapters) {
                     chapterSelect.innerHTML += `<option value="${chapter.id}">${chapter.name}</option>`;
                 }
                 
                })
                .catch(error => {
                    console.error("Error fetching chapters:", error);
                });
        }
     }
   