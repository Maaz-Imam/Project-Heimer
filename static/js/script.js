let container = document.getElementById('container')

toggle = () => {
	container.classList.toggle('sign-in')
	container.classList.toggle('sign-up')
}

setTimeout(() => {
	container.classList.add('sign-in')
}, 200)


let lg_userID = document.getElementById('login-email');
let lg_userPass = document.getElementById('login-password');
var OTP;
let sn_userName = document.getElementById('signup-name');
let sn_userID = document.getElementById('signup-email');
let sn_courseID = document.getElementById('signup-courseID');
let sn_userPass = document.getElementById('signup-password');
let sn_userConfirmPass = document.getElementById('signup-confirmPassword');
let sn_enterOTP = document.getElementById('signup-enterOTP');
let sn_button = document.getElementById('signup-button');
let sn_otp_button = document.getElementById('signup-OTP-button');

sn_enterOTP.style.display = 'none';
sn_otp_button.style.display = 'none';


function validateEmail(email) {
	const pattern = /^\w+([.-]?\w+)*@nu\.edu\.pk$/;
	return pattern.test(email);
}  


function login_button()
{
	document.getElementById('login-error-message').innerText = '';
	
	fetch('http://localhost:5000/api/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({"user_id":lg_userID.value,"user_pass":lg_userPass.value}),
	})
		.then(response => {
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		})
		.then(data => {
			console.log('Flag:', data)
			if(data == '1'){
				window.location.href = "/view/teacher_view";
			}
			else{
				document.getElementById('login-error-message').innerText = 'Incorrect username or password.';
			}
		})
		.catch(error => console.error('Error posting data:', error));
}



function signup_button()
{
	document.getElementById('signup-otp-message').innerText = '';
	document.getElementById('signup-error-message').innerText = '';

	if(validateEmail(sn_userID.value)){
		if(sn_userPass.value.length >= 8){
			if(sn_userPass.value != sn_userConfirmPass.value){
				document.getElementById('signup-error-message').innerText = "Passwords don't match";
			}
			else{
				sn_enterOTP.style.display = 'block';
				sn_otp_button.style.display = 'block';

				sn_userID.disabled = true;
				sn_userPass.disabled = true;
				sn_userConfirmPass.disabled = true;
				sn_button.disabled = true;
				sn_button.style.cursor = 'default';
				
				document.getElementById('signup-otp-message').innerText = 'Enter OTP sent at ' + sn_userID.value;
				
				fetch('http://localhost:5000/api/signup_attempt', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify({"user_id":sn_userID.value}),
				})
					.then(response => {
						if (!response.ok) {
							throw new Error('Network response was not ok');
						}
						return response.json();
					})
					.then(data => {
						console.log('OTP:', data)
						OTP = data;
					})
					.catch(error => console.error('Error posting data:', error));
			}
		}
		else{
			document.getElementById('signup-error-message').innerText = "Password length should be greater than 8 characters";
		}
	}
	else{
		document.getElementById('signup-error-message').innerText = "Enter a valid Email";
	}
}

function OTP_button()
{
	document.getElementById('signup-otp-message').innerText = '';
	document.getElementById('signup-error-message').innerText = '';

	if(sn_enterOTP.value == OTP){
		fetch('http://localhost:5000/api/signup_success', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({"user_name":sn_userName.value,"c_id":sn_courseID.value,"user_email":sn_userID.value,"user_pass":sn_userPass.value}),
		})
			.then(response => {
				if (!response.ok) {
					throw new Error('Network response was not ok');
				}
				return response.json();
			})
			.then(data => {
				console.log('OTP:', data)
			})
			.catch(error => console.error('Error posting data:', error));
			window.location.href = "/view/teacher_view";
	}
	else{
		document.getElementById('signup-error-message').innerText = 'Incorrect OTP';
	}
}