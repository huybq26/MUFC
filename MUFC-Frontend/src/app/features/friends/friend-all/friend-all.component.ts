import { Component } from '@angular/core';
import {MatCard, MatCardContent} from '@angular/material/card';
import jsonData from '../../../../assets/dummy-data/MUFC_Friend-dummy-data.json';
import friend_data from '../../../../assets/dummy-data/MUFC_Friend-dummy-data.json';
import {MatIconButton} from '@angular/material/button';
import {MatIcon} from '@angular/material/icon';
import {DatePipe, NgIf} from '@angular/common';

@Component({
  selector: 'app-friend-all',
  imports: [
    MatCard,
    MatIconButton,
    MatIcon,
    NgIf,
    DatePipe
  ],
  templateUrl: './friend-all.component.html',
  styleUrl: './friend-all.component.css'
})
export class FriendAllComponent {
  friend_data= jsonData;

  constructor() {
    console.log(this.friend_data);
  }

  isOverdue(lastContacted: string): boolean {
    const lastContactDate = this.parseDate(lastContacted);
    if (!lastContactDate) return false;

    const overdueDate = new Date(lastContactDate);
    overdueDate.setDate(overdueDate.getDate() + 30);

    const today = new Date();
    return today > overdueDate;
  }

  getOverdueDays(lastContacted: string): number {
    const lastContactDate = this.parseDate(lastContacted);
    if (!lastContactDate) return 0;

    const overdueDate = new Date(lastContactDate);
    overdueDate.setDate(overdueDate.getDate() + 30);

    const today = new Date();
    const diffTime = today.getTime() - overdueDate.getTime();
    return Math.floor(diffTime / (1000 * 60 * 60 * 24));
  }

  getNextContactDate(lastContacted: string): Date | null {
    const lastContactDate = this.parseDate(lastContacted);
    if (!lastContactDate) return null;

    lastContactDate.setDate(lastContactDate.getDate() + 30);
    return lastContactDate;
  }

  parseDate(dateStr: string): Date | null {
    const parts = dateStr.split('/'); // Split "29/06/2024"
    if (parts.length === 3) {
      const [day, month, year] = parts;
      return new Date(`${year}-${month}-${day}`); // Convert to "2024-06-29"
    }
    return null;
  }

}
