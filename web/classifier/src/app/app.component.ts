import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export class Hero {

  constructor(
    public id: number,
    public name: string,
    public power: string,
    public alterEgo?: string
  ) {  }

}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  result = '';
  url: string | ArrayBuffer | null = '';
  hasError = false;

  constructor(private readonly httpClient: HttpClient) {}

  postFile(event: any) {
  	const imagePath = event.target.files[0];
  	const reader = new FileReader();
    reader.readAsDataURL(imagePath); 
    reader.onload = () => { 
        this.url = reader.result; 
    }

	  this.httpClient.post('/classify', imagePath).subscribe((response: any) => {
	    this.result = response.label;
	  	this.hasError = false;
	  }, () => {
	    this.result = '';
	  	this.hasError = true;
	  });
  }
}
