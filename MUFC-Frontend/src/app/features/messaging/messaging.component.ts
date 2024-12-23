import {Component, NgModule, OnInit, signal} from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormField, MatLabel } from '@angular/material/form-field';
import { MatButton } from '@angular/material/button';
import { MatInput } from '@angular/material/input';
import { MatCard, MatCardContent, MatCardHeader, MatCardTitle } from '@angular/material/card';
import { ActivatedRoute } from '@angular/router';
import {MatDialog, MatDialogModule} from '@angular/material/dialog';

@NgModule({
  imports: [MatDialogModule]
})
export class AppModule {}
import jsonFriend from "../../../assets/dummy-data/MUFC_Friend-dummy-data.json"
import {ShareDialogComponent} from './share-dialog.component';

@Component({
  selector: 'app-messaging',
  imports: [
    ReactiveFormsModule,
    MatFormField,
    MatButton,
    MatInput,
    MatLabel,
    MatCard,
    MatCardHeader,
    MatCardContent,
    MatCardTitle
  ],
  templateUrl: './messaging.component.html',
  styleUrl: './messaging.component.css'
})
export class MessagingComponent implements OnInit {
  private friendData = jsonFriend;
  private currentFriend = signal<any>(this.friendData[0]);

  messagingForm = new FormGroup({
    recipient: new FormControl('', Validators.required),
    subject: new FormControl('', ),
    keywords: new FormControl(''),
    message: new FormControl('', Validators.required)
  });

  constructor(private route: ActivatedRoute, private dialog: MatDialog) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      if (params['friendId']) {
        this.searchFriendDetails(params['friendId'])
      }
      if (params['recipient']) {
        this.messagingForm.get('recipient')?.setValue(params['recipient']);
      }
      if (params['subject']) {
        this.messagingForm.get('subject')?.setValue(params['subject']);
      }
    });
  }

  searchFriendDetails(friendId: string) {
    // backend API, search the Friend for its name, hobbies
    // and list of available contact points,
    // i.e. currentFriend.email, currentFriend.facebook, currentFriend.whatsapp, currentFriend.insta, currentFriend.tele
    // and update the currentFriend variable
    this.currentFriend.set(this.friendData.find(friend => friend.friend_id === friendId));


  }

  onSend(): void {
    if (this.messagingForm.valid) {
      this.copyToClipboard(this.messagingForm.get('message')?.value || '');
      this.dialog.open(ShareDialogComponent, {
        data: { availablePlatforms: this.currentFriend() }
      });
    }
  }

  copyToClipboard(text: string): void {
    navigator.clipboard.writeText(text).then(() => {
      console.log('Message copied to clipboard!');
    }).catch(err => {
      console.error('Could not copy text: ', err);
    });
  }
}
