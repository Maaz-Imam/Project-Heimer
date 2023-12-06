function uploadFiles() {
    const courseCode = document.getElementById('upload-course-code').value;
    const studID = document.getElementById('student-id').value;
    const projectTitle = document.getElementById('project-title').value;
    const projectReport = document.getElementById('upload-report').files[0];
    const projectCode = document.getElementById('upload-project-code').files[0];

    if (projectReport && projectCode && courseCode.length>0 && studID.length>0 && projectTitle.length>0) {
        const formData = new FormData();
        formData.append('courseCode', courseCode);
        formData.append('studID', studID);
        formData.append('projectTitle', projectTitle);
        formData.append('report', projectReport);
        formData.append('code', projectCode);

        fetch('http://localhost:5000/view/teacher_view/uploadData', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('upload-status').innerText = 'Data uploaded successfully!';
            console.log('Response:', data);
        })
        .catch(error => {
            document.getElementById('upload-status').innerText = 'Error uploading data.';
            console.error('Error uploading file:', error);
        });
    } else {
        document.getElementById('upload-status').innerText = 'Please fill all fields.';
    }
}


function checkPlag() {
    const courseCode = document.getElementById('plag-course-code').value;
    const projectReport = document.getElementById('plag-report').files[0];
    const projectCode = document.getElementById('plag-project-code').files[0];

    if (projectReport && projectCode && courseCode.length>0) {
        const formData = new FormData();
        formData.append('courseCode', courseCode);
        formData.append('report', projectReport);
        formData.append('code', projectCode);

        fetch('http://localhost:5000/view/teacher_view/checkPlag', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('plag-status').innerText = 'Data uploaded successfully!';
            console.log('Response:', data);
        })
        .catch(error => {
            document.getElementById('plag-status').innerText = 'Error uploading data.';
            console.error('Error uploading file:', error);
        });
    } else {
        document.getElementById('plag-status').innerText = 'Please fill all fields.';
    }
}

function pastProj()
{
    updateProjectDetails('Project Title', 'CS101', '12345', 'report.pdf', 'code.zip');
    // fetch('http://localhost:5000/view/teacher_view/pastProj')
    // .then(response => {
    //     if (!response.ok) {
    //         throw new Error('Network response was not ok');
    //     }
    //     return response.json();
    // })
    // .then(data => {
    //     const fileList = document.getElementById('fileList');
    //     data.files.forEach(file => {
    //         const listItem = document.createElement('li');
    //         listItem.textContent = file;
    //         fileList.appendChild(listItem);
    //     });
    // })
    // .catch(error => console.error('Error fetching files:', error));    
}


function updateProjectDetails(projectTitle, courseCode, studentId, reportFile, codeFile) {
    const projectDetailsContainer = document.getElementById('projectDetails');
    
    // Create a card to display project details
    const card = document.createElement('div');
    card.classList.add('card');

    // Populate card with project details
    card.innerHTML = `
        <h3>${projectTitle}</h3>
        <p>Course Code: ${courseCode}</p>
        <p>Student ID: ${studentId}</p>
        <p>Report File: ${reportFile}</p>
        <p>Code File: ${codeFile}</p>
    `;

    // Append the card to the project details container
    projectDetailsContainer.appendChild(card);
}