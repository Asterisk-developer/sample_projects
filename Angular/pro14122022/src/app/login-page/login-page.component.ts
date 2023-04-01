import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { passwordStrengthValidator } from '../utils/passwordStrength.validaor';


@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {
  amount:number = 200;
  appHighlight = 'blue'

  loginPageForm = new FormGroup({
    userName: new FormControl('',[Validators.required]),
    password: new FormControl('',[Validators.required,passwordStrengthValidator()])
  })

  constructor() { }

  ngOnInit(): void {
  }
  login(){
    alert('logged in')
  }

}
